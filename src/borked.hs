{-# LANGUAGE OverloadedStrings #-}
module Main where

import Control.Applicative
import Control.Concurrent
import Control.Monad.Trans
import Data.ByteString.Char8 (ByteString)
import qualified   Data.ByteString.Char8 as B
import Snap.Types
import Snap.Util.FileServe
import Snap.StaticPages
import System.Posix.Env
import Text.Templating.Heist
import Text.Templating.Heist.TemplateDirectory

import Glue hiding (templateServe)
import Server


{-

Eventually we'll do this to publish our content

ln25:  templateServe (bindSplices appSplices ts) <|>

appSplices :: Monad m => [(ByteString, Splice m)]
appSplices = [("frontPagePosts", frontPagePosts)]

-}

data SiteState = SiteState {
    _origTs         :: TemplateState Snap
  , _currentTs      :: MVar (TemplateState Snap)
  , _staticState    :: MVar StaticPagesState
}


initSiteState :: IO SiteState
initSiteState = do
    setLocaleToUTF8

    ets <- loadTemplates "templates" emptyTemplateState
    let ts = either error id ets
    tsMVar <- newMVar $ ts

    bs <- loadStaticPages' ts "acm"

    return $ SiteState emptyTemplateState tsMVar bs


renderTmpl :: MVar (TemplateState Snap)
           -> ByteString
           -> Snap ()
renderTmpl tsMVar n = do
    ts <- liftIO $ readMVar tsMVar
    maybe pass writeBS =<< renderTemplate ts n


templateServe :: MVar (TemplateState Snap)
              -> Snap ()
templateServe tsMVar = do
    p
    modifyResponse $ setContentType "text/html"

  where
    p = ifTop (renderTmpl tsMVar "index") <|>
        (renderTmpl tsMVar . B.pack =<< getSafePath)



site :: SiteState -> Snap ()
site ss =
  ifTop (renderTmpl (_currentTs ss) "home") <|>
  route [ ("meh/", serveStaticPages (_staticState ss)) ] <|>
  templateServe (_currentTs ss) <|>
  dir "static" (fileServe ".")





setLocaleToUTF8 :: IO ()
setLocaleToUTF8 = do
    mapM_ (\k -> setEnv k "en_US.UTF-8" True)
          [ "LANG"
          , "LC_CTYPE"
          , "LC_NUMERIC"
          , "LC_TIME"
          , "LC_COLLATE"
          , "LC_MONETARY"
          , "LC_MESSAGES"
          , "LC_PAPER"
          , "LC_NAME"
          , "LC_ADDRESS"
          , "LC_TELEPHONE"
          , "LC_MEASUREMENT"
          , "LC_IDENTIFICATION"
          , "LC_ALL" ]
      
      
main :: IO ()
main = do
  ss <- initSiteState
  quickServer $ site ss

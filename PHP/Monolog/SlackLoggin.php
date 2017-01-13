<?php
require __DIR__ . "/vendor/autoload.php";

use Monolog\Handler\SlackHandler;
use Monolog\Logger;

$logger = new Monolog\logger('slack-test');
$slackHandler = new SlackHandler(
    "Slack_AUTH_KEY", // Look for it at https://api.slack.com/web#auth
    "#chanelName", // It needs to go with the `#`
    "BotName"
);
$logger->pushHandler($slackHandler);

$slackHandler->setLevel(\Monolog\Logger::ERROR);

$logger->error("This is an error message");
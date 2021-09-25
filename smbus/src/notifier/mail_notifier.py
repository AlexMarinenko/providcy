# -*- coding: utf-8 -*-
"""
Descrition
"""
__author__ = 'maxdob'
__date__ = '25.09.21'
__time__ = '21:32'
__version__ = '0.1'

import smtplib
import ssl
from logging import getLogger
from .base_notifier import BaseNotifier
import settings


class MailNotifier(BaseNotifier):
    """MailNotifier class for sending email messages."""

    logger = getLogger('notifier.mail_notifier.MailNotifier')

    def __init__(self, subject: str, message: str):
        super().__init__(subject, message)
        self.logger.debug("Init mail notifier.")
        self.__port = settings.email_port
        self.__smtp_server = settings.email_smtp_server

    def send(self) -> bool:
        """
        Sending an email message
        Returns
        -------
        result: bool
            Result email sending.
        """

        self.logger.debug("Sending email notification.")
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
                server.login(settings.email_login, settings.email_password)
                server.sendmail(settings.email_sender, settings.email_receiver, self._message.encode("utf8"))
        except Exception as exp:
            self.logger.warning(exp)
            return False
        else:
            self.logger.debug("Successful.")
            return True

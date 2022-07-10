"""
Django command to wait for the database service to be available.
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to wait for the database """

    def handle(self, *args, **options):
        """ Entrypoint for command """

        self.stdout.write('Waiting for database...')

        db_up = False
        attempt_counter = 1

        while not db_up and attempt_counter < 10:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                attempt_counter += 1
                self.stdout.write('Database unavailable,',
                                  'waiting for 1 second...')
                time.sleep(1)

        if attempt_counter >= 10:
            self.stdout.write('Something wrong with the ',
                              'database settings. Please check!')
            raise OperationalError

        self.stdout.write(self.style.SUCCESS('Database available'))

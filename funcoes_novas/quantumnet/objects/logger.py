import logging

FORMAT = '%(asctime)s: %(message)s'
logging.basicConfig(format=FORMAT)

class Logger(object):
    __instance = None
    DISABLED = True

    def __init__(self):
            if Logger.__instance is None:
                self.logger = logging.getLogger('qkdnet')
                self.logger.setLevel(logging.DEBUG)
                Logger.__instance = self
            else:
                raise Exception('Esta é uma classe singleton')

    def get_instance():
            """
            Retorna uma instância do Logger.

            Se a instância ainda não foi criada, cria uma nova instância e a retorna.
            Caso contrário, retorna a instância existente.

            Returns:
                Logger: A instância do Logger.
            """
            if Logger.__instance is None:
                Logger()
            return Logger.__instance

    def activate(self):
        Logger.DISABLED = False
    
    def warn(self, message):
            """
            Registra uma mensagem de aviso no logger.

            Parâmetros:
            - message: A mensagem de aviso a ser registrada.

            """
            if not Logger.DISABLED:
                self.logger.warning(message)

    def error(self, message):
            """
            Registra uma mensagem de erro no log.

            Parâmetros:
            - message: A mensagem de erro a ser registrada.

            """
            if not Logger.DISABLED:
                self.logger.error(message)

    def log(self, message):
            """
            Registra uma mensagem de log.

            Parâmetros:
            - message: A mensagem a ser registrada.

            """
            if not Logger.DISABLED:
                self.logger.info(message)

    def debug(self, message):
            """
            Registra uma mensagem de depuração.

            Args:
                message (str): A mensagem a ser registrada.

            Returns:
                None
            """
            if not Logger.DISABLED:
                self.logger.debug(message)

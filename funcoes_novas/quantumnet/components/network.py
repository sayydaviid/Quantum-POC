import networkx as nx
from ..objects import Logger
from ..components import Host

class Network():
    """
    Um objeto para utilizar como rede.
    """
    def __init__(self) -> None:
        # Sobre a rede
        self._graph = nx.Graph()
        self._channels = None
        self._topology = None
        self._hosts = {}
        self._controller = None
        # Sobre a execução
        self.logger = Logger.get_instance()
        
    @property
    def hosts(self):
        """
        Dicionário com os hosts da rede. No padrão {host_id: host}.

        Returns:
            dict : Dicionário com os hosts da rede.
        """
        return self._hosts
    
    def draw(self):
        """
        Desenha a rede.
        """
        nx.draw(self._graph, with_labels=True)
    
    def add_host(self, host: Host):
        """
        Adiciona um host à rede no dicionário de hosts, e o host_id ao grafo da rede.
            
            Args:
                host (Host): O host a ser adicionado.
        """
        # Adiciona o host ao dicionário de hosts, se não existir
        if host.host_id not in self._hosts:
            self._hosts[host.host_id] = host
            Logger.get_instance().debug(f'Host {host.host_id} adicionado aos hosts da rede.')
        
        # Adiciona o nó ao grafo da rede, se não existir
        if not self._graph.has_node(host.host_id):
            self._graph.add_node(host.host_id)
            Logger.get_instance().debug(f'Nó {host.host_id} adicionado ao grafo da rede.')
        
        # Adiciona as conexões do nó ao grafo da rede, se não existirem
        for connection in host.connections:
            if not self._graph.has_edge(host.host_id, connection):
                self._graph.add_edge(host.host_id, connection)
                Logger.get_instance().debug(f'Conexões do {host.host_id} adicionados ao grafo da rede.')
        
    def add_controller(self, controller: Host):
        """
        Adiciona um controlador à rede.

        Args:
            controller (Host): O controlador a ser adicionado.
        """
        self._controller = controller
        self.add_host(controller)
        Logger.get_instance().debug(f'Controlador {controller.host_id} adicionado à rede.')
    
    def get_host(self, host_id: str) -> Host:
        """
        Retorna um host da rede.

        Args:
            host_id (str): O host_id do host a ser retornado.

        Returns:
            Host : O host.
        """
        return self._hosts[host_id]
    
    def get_controller(self) -> Host:
        """
        Retorna o controlador da rede.

        Returns:
            Host : O controlador.
        """
        return self._controller
    
    def get_hosts(self) -> dict:
        """
        Retorna os hosts da rede.

        Returns:
            dict : Dicionário com os hosts da rede.
        """
        return self._hosts
    
    def get_graph(self) -> nx.Graph:
        """
        Retorna o grafo da rede.

        Returns:
            nx.Graph : Grafo da rede.
        """
        return self._graph
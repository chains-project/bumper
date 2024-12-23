```java
import develop.p2p.lib.*;
import develop.p2p.lib.common.Constants;
import develop.p2p.lib.common.Message;
import develop.p2p.lib.common.P2P;
import develop.p2p.lib.common.Peer;
import develop.p2p.lib.common.PeerListener;
import develop.p2p.lib.common.exception.P2PException;
import develop.p2p.lib.common.util.CommonUtils;
import develop.p2p.lib.common.util.NetUtils;
import develop.p2p.lib.common.util.ThreadUtils;
import develop.p2p.lib.server.P2PServer;
import develop.p2p.lib.server.ServerListener;
import develop.p2p.lib.server.ServerPeer;
import develop.p2p.lib.server.ServerPeerListener;
import develop.p2p.lib.server.exception.ServerException;
import develop.p2p.lib.server.util.ServerUtils;
import develop.p2p.lib.server.util.SocketUtils;
import develop.p2p.lib.server.util.ThreadUtils;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class NPCTeleport {

    private static final Logger logger = LoggerFactory.getLogger(NPCTeleport.class);

    private static final int PORT = 8888;

    private static final String HOST = "localhost";

    private static final int MAX_CONNECTIONS = 10;

    private static final List<Peer> peers = new ArrayList<>();

    private static final ExecutorService executorService = Executors.newFixedThreadPool(MAX_CONNECTIONS);

    public static void main(String[] args) throws IOException, P2PException, InterruptedException {
        P2PServer server = new P2PServer(PORT, HOST);
        server.setServerListener(new ServerListener() {
            @Override
            public void onServerStarted(P2PServer server) {
                logger.info("Server started on port {}", server.getPort());
            }

            @Override
            public void onServerStopped(P2PServer server) {
                logger.info("Server stopped");
            }

            @Override
            public void onPeerConnected(ServerPeer peer) {
                logger.info("Peer connected: {}", peer.getAddress());
                peers.add(peer);
            }

            @Override
            public void onPeerDisconnected(ServerPeer peer) {
                logger.info("Peer disconnected: {}", peer.getAddress());
                peers.remove(peer);
            }

            @Override
            public void onMessageReceived(ServerPeer peer, Message message) {
                logger.info("Message received from {}: {}", peer.getAddress(), message);
            }
        });
        server.start();

        logger.info("Server running...");

        while (true) {
            // Send a message to all connected peers every 5 seconds
            for (Peer peer : peers) {
                Message message = new Message(Constants.MESSAGE_TYPE_TEXT, "Hello from server!");
                server.sendMessage(peer, message);
            }

            ThreadUtils.sleep(5000);
        }
    }
}
```
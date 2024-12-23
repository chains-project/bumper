```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.DTLSClientProtocol;
import org.bouncycastle.crypto.tls.DTLSRecordLayer;
import org.bouncycastle.crypto.tls.DatagramTransport;
import org.bouncycastle.crypto.tls.ProtocolVersion;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.concurrent.atomic.AtomicBoolean;

public class ChachaDecoder {

    private final DatagramSocket socket;
    private final InetAddress address;
    private final int port;
    private final AtomicBoolean closed = new AtomicBoolean(false);

    private DTLSRecordLayer recordLayer;
    private DTLSClientProtocol protocol;

    public ChachaDecoder(DatagramSocket socket, InetAddress address, int port) throws IOException {
        this.socket = socket;
        this.address = address;
        this.port = port;
    }

    public void start() throws IOException {
        recordLayer = new DTLSRecordLayer(new DatagramTransport() {
            @Override
            public int getReceiveLimit() throws IOException {
                return socket.getReceiveBufferSize();
            }

            @Override
            public int getSendLimit() throws IOException {
                return socket.getSendBufferSize();
            }

            @Override
            public void receive(byte[] buf, int off, int len, int waitMillis) throws IOException {
                DatagramPacket packet = new DatagramPacket(buf, off, len, address, port);
                socket.receive(packet);
            }

            @Override
            public void send(byte[] buf, int off, int len) throws IOException {
                DatagramPacket packet = new DatagramPacket(buf, off, len, address, port);
                socket.send(packet);
            }

            @Override
            public void close() throws IOException {
                socket.close();
            }
        }, new ProtocolVersion(ProtocolVersion.DTLSv12.getMajorVersion(), ProtocolVersion.DTLSv12.getMinorVersion()));
        protocol = new DTLSClientProtocol(recordLayer);
        protocol.connect(new TlsClient());
    }

    public void stop() {
        closed.set(true);
        protocol.close();
        recordLayer.close();
    }

    public byte[] decode(byte[] data) throws IOException {
        if (closed.get()) {
            throw new SocketException("Socket closed");
        }
        recordLayer.receive(data, 0, data.length, 0);
        return recordLayer.getReadPlaintext();
    }

    private class TlsClient extends DTLSClientProtocol.AbstractClient {

        @Override
        public void handleAlert(short alertLevel, short alertDescription) {
            if (alertLevel == AlertDescription.fatal) {
                stop();
            }
        }

        @Override
        public void receiveServerHello(org.bouncycastle.crypto.tls.ServerHello serverHello) {
            // Do nothing
        }

        @Override
        public void receiveServerCertificate(org.bouncycastle.crypto.tls.Certificate certificate) {
            // Do nothing
        }

        @Override
        public void receiveServerKeyExchange(org.bouncycastle.crypto.tls.ServerKeyExchange serverKeyExchange) {
            // Do nothing
        }

        @Override
        public void receiveCertificateRequest(org.bouncycastle.crypto.tls.CertificateRequest certificateRequest) {
            // Do nothing
        }

        @Override
        public void receiveServerHelloDone() {
            // Do nothing
        }

        @Override
        public void receiveFinished(byte[] finished) {
            // Do nothing
        }

        @Override
        public void receiveSupplementalData(Vector supplementalData) {
            // Do nothing
        }

        @Override
        public void receiveHeartbeat(byte[] heartbeat) {
            // Do nothing
        }

        @Override
        public void receiveNewSessionTicket(NewSessionTicket newSessionTicket) {
            // Do nothing
        }

        @Override
        public void receiveKeyUpdate(KeyUpdate keyUpdate) {
            // Do nothing
        }

        @Override
        public void receiveCertificateStatus(CertificateStatus certificateStatus) {
            // Do nothing
        }

        @Override
        public void receiveCertificateStatusRequest(CertificateStatusRequest certificateStatusRequest) {
            // Do nothing
        }

        @Override
        public void receiveClientHello(ClientHello clientHello) {
            // Do nothing
        }

        @Override
        public void receiveClientSupplementalData(Vector clientSupplementalData) {
            // Do nothing
        }

        @Override
        public void receiveFinished(long finished) {
            // Do nothing
        }

        @Override
        public void receiveHelloVerifyRequest(HelloVerifyRequest helloVerifyRequest) {
            // Do nothing
        }

        @Override
        public void receiveChangeCipherSpec() {
            // Do nothing
        }

        @Override
        public void receiveNextProtocol(String protocol) {
            // Do nothing
        }

        @Override
        public void receiveSessionTicket(SessionTicket sessionTicket) {
            // Do nothing
        }

        @Override
        public void receiveNewSessionTicket(NewSessionTicket newSessionTicket) {
            // Do nothing
        }

        @Override
        public void receiveKeyUpdate(KeyUpdate keyUpdate) {
            // Do nothing
        }

        @Override
        public void receiveCertificateStatus(CertificateStatus certificateStatus) {
            // Do nothing
        }

        @Override
        public void receiveCertificateStatusRequest(CertificateStatusRequest certificateStatusRequest) {
            // Do nothing
        }
    }
}
```
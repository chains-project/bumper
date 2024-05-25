```java
  import org.apache.thrift.transport.TTransport;

  import com.pinterest.singer.thrift.Singer;

  import org.apache.thrift.protocol.TBinaryProtocol;
  import org.apache.thrift.protocol.TProtocol;
  import org.apache.thrift.transport.TSocket;
  import org.apache.thrift.transport.TFramedTransport;

  import java.io.IOException;
  import java.net.ConnectException;
  import java.net.Socket;
  import java.net.SocketTimeoutException;
  import java.util.concurrent.TimeUnit;

  public class ThriftReader extends AbstractDataReader<ThriftReaderConfig, Singer.Client> {

      private final String host;
      private final int port;
      private final int timeout;
      private final int maxReadAttempts;
      private final int readAttemptInterval;

      public ThriftReader(ThriftReaderConfig config) {
          super(config);
          this.host = config.getHost();
          this.port = config.getPort();
          this.timeout = config.getTimeout();
          this.maxReadAttempts = config.getMaxReadAttempts();
          this.readAttemptInterval = config.getReadAttemptInterval();
      }

      @Override
      protected Singer.Client createClient() throws IOException {
          TTransport transport = new TFramedTransport(new TSocket(host, port, timeout));
          TProtocol protocol = new TBinaryProtocol(transport);
          return new Singer.Client(protocol);
      }

      @Override
      protected void closeClient(Singer.Client client) throws IOException {
          client.getInputProtocol().getTransport().close();
      }

      @Override
      protected List<Singer.Message> readData(Singer.Client client) throws IOException {
          List<Singer.Message> messages = new ArrayList<>();
          int readAttempts = 0;
          while (readAttempts < maxReadAttempts) {
              try {
                  messages.addAll(client.read());
                  break;
              } catch (ConnectException e) {
                  readAttempts++;
                  if (readAttempts < maxReadAttempts) {
                      try {
                          TimeUnit.SECONDS.sleep(readAttemptInterval);
                      } catch (InterruptedException ignored) {
                          Thread.currentThread().interrupt();
                          break;
                      }
                  }
              } catch (SocketTimeoutException e) {
                  readAttempts++;
                  if (readAttempts < maxReadAttempts) {
                      try {
                          TimeUnit.SECONDS.sleep(readAttemptInterval);
                      } catch (InterruptedException ignored) {
                          Thread.currentThread().interrupt();
                          break;
                      }
                  }
              }
          }
          return messages;
      }
  }
```
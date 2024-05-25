```java
  import org.apache.thrift.transport.TTransport;

  import java.io.IOException;

  public class AppenderUtils {

    /**
     * Creates a TTransport instance based on the given configuration.
     *
     * @param config the configuration
     * @return the TTransport instance
     * @throws IOException if an error occurs
     */
    public static TTransport createTTransport(Config config) throws IOException {
      String transportType = config.getString("transport.type");

      switch (transportType) {
        case "framed":
          return new TFastFramedTransport(config.getInputStream());
        case "buffered":
          return new TTransport(config.getInputStream());
        default:
          throw new IllegalArgumentException("Unknown transport type: " + transportType);
      }
    }
  }
```
```java
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TCompactProtocol;
import org.apache.thrift.protocol.TJSONProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.protocol.TProtocolFactory;
import org.apache.thrift.transport.TIOStreamTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransientTransport;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

/**
 * A Thrift reader that reads data from a Thrift server.
 */
public class ThriftReader<T> extends AbstractReader<T> {

  private final TProtocolFactory protocolFactory;
  private final TProtocol protocol;
  private final TTransport transport;
  private final TCompactProtocol compactProtocol;
  private final TBinaryProtocol binaryProtocol;
  private final TJSONProtocol jsonProtocol;

  /**
   * Constructor.
   *
   * @param schema the schema of the data to be read
   * @param stream the input stream to read from
   * @param protocolFactory the protocol factory to use to create the protocol
   */
  public ThriftReader(Schema schema, InputStream stream, TProtocolFactory protocolFactory) {
    super(schema);
    this.protocolFactory = protocolFactory;
    this.transport = new TIOStreamTransport(stream);
    this.protocol = protocolFactory.getProtocol(transport);
    this.compactProtocol = new TCompactProtocol(transport);
    this.binaryProtocol = new TBinaryProtocol(transport);
    this.jsonProtocol = new TJSONProtocol(transport);
  }

  /**
   * Constructor.
   *
   * @param schema the schema of the data to be read
   * @param socket the socket to read from
   * @param protocolFactory the protocol factory to use to create the protocol
   */
  public ThriftReader(Schema schema, Socket socket, TProtocolFactory protocolFactory) {
    super(schema);
    this.protocolFactory = protocolFactory;
    this.transport = new TTransport(socket);
    this.protocol = protocolFactory.getProtocol(transport);
    this.compactProtocol = new TCompactProtocol(transport);
    this.binaryProtocol = new TBinaryProtocol(transport);
    this.jsonProtocol = new TJSONProtocol(transport);
  }

  /**
   * Constructor.
   *
   * @param schema the schema of the data to be read
   * @param host the hostname of the server to read from
   * @param port the port of the server to read from
   * @param protocolFactory the protocol factory to use to create the protocol
   */
  public ThriftReader(Schema schema, String host, int port, TProtocolFactory protocolFactory) {
    super(schema);
    this.protocolFactory = protocolFactory;
    try {
      this.transport = new TSocket(host, port);
      this.protocol = protocolFactory.getProtocol(transport);
      this.compactProtocol = new TCompactProtocol(transport);
      this.binaryProtocol = new TBinaryProtocol(transport);
      this.jsonProtocol = new TJSONProtocol(transport);
    } catch (TTransportException e) {
      throw new RuntimeException(e);
    }
  }

  /**
   * Open the reader.
   */
  @Override
  public void open() {
    try {
      transport.open();
    } catch (TTransportException e) {
      throw new RuntimeException(e);
    }
  }

  /**
   * Close the reader.
   */
  @Override
  public void close() {
    try {
      transport.close();
    } catch (TTransportException e) {
      throw new RuntimeException(e);
    }
  }

  /**
   * Read a record from the reader.
   *
   * @return the record
   */
  @Override
  public T read() {
    try {
      T record = schema.getRecordClass().newInstance();
      record.read(protocol);
      return record;
    } catch (TException e) {
      throw new RuntimeException(e);
    } catch (InstantiationException e) {
      throw new RuntimeException(e);
    } catch (IllegalAccessException e) {
      throw new RuntimeException(e);
    }
  }

  /**
   * Read a record from the reader using the compact protocol.
   *
   * @return the record
   */
  public T readCompact() {
    try {
      T record = schema.getRecordClass().newInstance();
      record.read(compactProtocol);
      return record;
    } catch (TException e) {
      throw new RuntimeException(e);
    } catch (InstantiationException e) {
      throw new RuntimeException(e);
    } catch (IllegalAccessException e) {
      throw new RuntimeException(e);
    }
  }

  /**
   * Read a record from the reader using the binary protocol.
   *
   * @return the record
   */
  public T readBinary() {
    try {
      T record = schema.getRecordClass().newInstance();
      record.read(binaryProtocol);
      return record;
    } catch (TException e) {
      throw new RuntimeException(e);
    } catch (InstantiationException e) {
      throw new RuntimeException(e);
    } catch (IllegalAccessException e) {
      throw new RuntimeException(e);
    }
  }

  /**
   * Read a record from the reader using the json protocol.
   *
   * @return the record
   */
  public T readJSON() {
    try {
      T record = schema.getRecordClass().newInstance();
      record.read(jsonProtocol);
      return record;
    } catch (TException e) {
      throw new RuntimeException(e);
    } catch (InstantiationException e) {
      throw new RuntimeException(e);
    } catch (IllegalAccessException e) {
      throw new RuntimeException(e);
    }
  }

  /**
   * Get the protocol factory used by the reader.
   *
   * @return the protocol factory
   */
  public TProtocolFactory getProtocolFactory() {
    return protocolFactory;
  }

  /**
   * Get the protocol used by the reader.
   *
   * @return the protocol
   */
  public TProtocol getProtocol() {
    return protocol;
  }

  /**
   * Get the transport used by the reader.
   *
   * @return the transport
   */
  public TTransport getTransport() {
    return transport;
  }

  /**
   * Get the compact protocol used by the reader.
   *
   * @return the compact protocol
   */
  public TCompactProtocol getCompactProtocol() {
    return compactProtocol;
  }

  /**
   * Get the binary protocol used by the reader.
   *
   * @return the binary protocol
   */
  public TBinaryProtocol getBinaryProtocol() {
    return binaryProtocol;
  }

  /**
   * Get the json protocol used by the reader.
   *
   * @return the json protocol
   */
  public TJSONProtocol getJSONProtocol() {
    return jsonProtocol;
  }

  /**
   * A transport that wraps a socket.
   */
  private static class TTransport extends TTransientTransport {

    private final Socket socket;

    /**
     * Constructor.
     *
     * @param socket the socket to wrap
     */
    public TTransport(Socket socket) {
      this.socket = socket;
    }

    /**
     * Open the transport.
     */
    @Override
    public void open() throws TTransportException {
      try {
        inputStream = socket.getInputStream();
        outputStream = socket.getOutputStream();
      } catch (IOException e) {
        throw new TTransportException(e);
      }
    }

    /**
     * Close the transport.
     */
    @Override
    public void close() {
      try {
        inputStream.close();
        outputStream.close();
        socket.close();
      } catch (IOException e) {
        throw new RuntimeException(e);
      }
    }

    /**
     * Get the input stream.
     *
     * @return the input stream
     */
    @Override
    protected InputStream getInputStream() {
      return inputStream;
    }

    /**
     * Get the output stream.
     *
     * @return the output stream
     */
    @Override
    protected OutputStream getOutputStream() {
      return outputStream;
    }

    private InputStream inputStream;
    private OutputStream outputStream;
  }
}
```
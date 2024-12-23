```java
import com.jcabi.aspects.Tv;
import com.jcabi.log.Logger;

public class SshByPassword implements Ssh {
  private final Ssh ssh;
  public SshByPassword(Ssh ssh, char[] password) {
    this.ssh = ssh;
    ssh.auth().password(password);
  }
  public Tv tv() {
    return ssh.tv();
  }
  public void close() throws IOException {
    ssh.close();
  }
  public void connect() throws IOException {
    ssh.connect();
  }
  public void disconnect() throws IOException {
    ssh.disconnect();
  }
  public String getHost() {
    return ssh.getHost();
  }
  public int getPort() {
    return ssh.getPort();
  }
  public String getUser() {
    return ssh.getUser();
  }
  public boolean isConnected() {
    return ssh.isConnected();
  }
  public boolean isDisconnected() {
    return ssh.isDisconnected();
  }
  public boolean isInteractive() {
    return ssh.isInteractive();
  }
  public boolean isRemote() {
    return ssh.isRemote();
  }
  public boolean isShell() {
    return ssh.isShell();
  }
  public boolean isSftp() {
    return ssh.isSftp();
  }
  public void setHost(String host) {
    ssh.setHost(host);
  }
  public void setPort(int port) {
    ssh.setPort(port);
  }
  public void setUser(String user) {
    ssh.setUser(user);
  }
  public void setTimeout(int timeout) {
    ssh.setTimeout(timeout);
  }
  public void setInteractive(boolean interactive) {
    ssh.setInteractive(interactive);
  }
  public void setLocalPortForwarding(int localPort, String remoteHost, int remotePort) {
    ssh.setLocalPortForwarding(localPort, remoteHost, remotePort);
  }
  public void setRemotePortForwarding(int remotePort, String localHost, int localPort) {
    ssh.setRemotePortForwarding(remotePort, localHost, localPort);
  }
  public void setProxy(String host, int port, String user, char[] password) {
    ssh.setProxy(host, port, user, password);
  }
}
```
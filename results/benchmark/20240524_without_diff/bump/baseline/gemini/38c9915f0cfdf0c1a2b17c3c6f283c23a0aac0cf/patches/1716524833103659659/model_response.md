```java
  import org.cactoos.text.UncheckedText;

  import java.io.IOException;
  import java.util.List;

  public class WalletsIn {

    private final List<String> walletAddresses;

    public WalletsIn(List<String> walletAddresses) {
      this.walletAddresses = walletAddresses;
    }

    public List<String> getWalletAddresses() {
      return walletAddresses;
    }

    public String getWalletAddress(int index) {
      return walletAddresses.get(index);
    }

    public int getWalletCount() {
      return walletAddresses.size();
    }

    public String getWalletAddress(String walletAddress) {
      return walletAddresses.stream()
          .filter(address -> address.equalsIgnoreCase(walletAddress))
          .findFirst()
          .orElseThrow(() -> new IllegalArgumentException("Wallet address not found: " + walletAddress));
    }

    public List<String> getWalletsIn(String walletAddress) {
      return walletAddresses.stream()
          .filter(address -> address.startsWith(walletAddress))
          .collect(Collectors.toList());
    }

    public String getWalletAddressFromMnemonic(String mnemonic) throws IOException {
      String walletAddress = new UncheckedText(
          () -> Runtime.getRuntime().exec(new String[]{"zold", "wallet", "address", "-m", mnemonic})
              .getInputStream()).asString();
      return walletAddress.trim();
    }
  }
```
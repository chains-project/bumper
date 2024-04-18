```java
  import org.cactoos.text.TextOf;

  public class WalletsIn {
    // ...

    @Override
    public List<Wallet> call() throws Exception {
      List<Wallet> wallets = new ArrayList<>();
      for (String walletId : new JoinedText(
          " ",
          new TextOf(this.wallets.get(0).getId()),
          new TextOf(this.wallets.get(1).getId())
      )) {
        wallets.add(this.wallets.stream()
            .filter(wallet -> wallet.getId().equals(walletId))
            .findFirst()
            .orElseThrow(() -> new WalletNotFoundException(walletId))
        );
      }
      return wallets;
    }

    // ...
  }
```
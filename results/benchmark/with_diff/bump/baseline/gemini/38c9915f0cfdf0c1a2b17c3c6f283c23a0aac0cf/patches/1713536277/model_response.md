```java
  import org.cactoos.scalar.Scalar;

  public class WalletsIn extends Wallets {

    public WalletsIn(final Scalar<String> seed, final Scalar<String> passphrase) {
      super(new Wallets.Data(seed, passphrase));
    }
  }
```
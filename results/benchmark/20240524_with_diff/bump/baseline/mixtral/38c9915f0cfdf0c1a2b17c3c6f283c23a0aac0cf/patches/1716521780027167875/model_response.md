Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public RtTransaction(RtEnv env, RtTxIn txIn, RtTxOut txOut, RtTxOut[] txOuts,
    RtTxOut[] vin, byte[] witness, String lockTime) {
  // ...
  int length = new LengthOf(vin).intValue();
  // ...
}
```
I replaced the import statement with the new equivalent, and updated the method to use the new `LengthOf` method.
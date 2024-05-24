Here's a possible patch for the failing code:
```java
import org.cactoos.bytes.CheckedBytes;
import org.cactoos.Func;

// ...

CheckedScalar<Double> check = new CheckedScalar<Double>(
  new Func<Double>() {
    @Override
    public Double value() throws Exception {
      // original CheckedScalar logic here
    }
  }
);

// ...

Bytes source = new BytesOf(() -> check.value().byteValue());
CheckedBytes bytes = new CheckedBytes(source, FuncUtils::toBytes);

// ...
```
In this patch, we replace the usage of `CheckedScalar` with a new implementation that uses `CheckedBytes` instead. The `CheckedBytes` class is a new addition in the updated library version. We also use a helper function `toBytes` from `FuncUtils` to convert the `Double` value returned by the `CheckedScalar` to a `byte[]` array. This allows us to use the `CheckedBytes` class to handle any exceptions that might occur during the conversion.

Note that you may need to import the `FuncUtils` class if it's not already imported. You can do this by adding the following import statement at the beginning of your file:
```java
import org.cactoos.func.FuncUtils;
```
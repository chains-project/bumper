Here's a proposed patch to fix the error:
```java
import org.cactoos.scalar.IoCheckedScalar;

// ...

IoCheckedScalar<String> scalar = IoCheckedScalar.of(" Failure message ");
```
Replace the failing line with the following code:
```java
IoCheckedScalar<String> scalar = new IoCheckedScalar<>(() -> " Failure message ");
```
The `IoCheckedScalar` class has been removed in the new library version, so we need to create a new instance of it using the constructor that takes a supplier of the value to be wrapped. The `() -> " Failure message"` syntax creates a supplier that returns the string " Failure message ".

This patch should fix the error and allow the code to compile and run successfully.
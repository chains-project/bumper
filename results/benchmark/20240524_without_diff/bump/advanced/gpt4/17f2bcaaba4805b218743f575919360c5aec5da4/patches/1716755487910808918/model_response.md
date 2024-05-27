This error message indicates that there is a syntax error in your code. It seems that the import statement is standing alone without being part of a class, interface, or enum. Here is a patch:

```java
public class PGS_MorphologyGroupShapeTests {

    import org.junit.jupiter.api.Test;

    // your test methods here
}
```
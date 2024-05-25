```java
  import io.zold.api.RtTransaction;
  import org.cactoos.iterable.LengthOf;
  import org.junit.jupiter.api.Test;

  import static org.junit.jupiter.api.Assertions.assertEquals;

  class RtTransactionTest {

    @Test
    void test() {
      // Given
      RtTransaction transaction = new RtTransaction();

      // When
      int length = new LengthOf<>(transaction.getOutputs()).value();

      // Then
      assertEquals(0, length);
    }
  }
```
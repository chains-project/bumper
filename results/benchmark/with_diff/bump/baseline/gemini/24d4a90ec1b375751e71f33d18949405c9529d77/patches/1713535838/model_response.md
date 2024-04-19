```java
  import org.junit.jupiter.api.Test;

  import static org.mockito.Mockito.mock;
  import static org.mockito.Mockito.verify;

  @Test
  void test() {
    final Tv tv = mock(Tv.class);
    tv.turnOn();
    verify(tv).turnOn();
  }
```
```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.github.mock.MkGithub;
  import java.io.IOException;
  import java.util.concurrent.TimeoutException;
  import org.junit.jupiter.api.BeforeEach;
  import org.junit.jupiter.api.Test;
  import org.junit.jupiter.api.extension.ExtendWith;
  import org.mockito.Mock;
  import org.mockito.junit.jupiter.MockitoExtension;

  @ExtendWith(MockitoExtension.class)
  public class MkGithubTest {

    @Mock
    private Tv tv;

    @BeforeEach
    public void setUp() throws IOException, TimeoutException {
      MkGithub.main(tv);
    }

    @Test
    public void test() {
    }
  }
```
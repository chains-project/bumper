```java
import com.jcabi.aspects.Tv;
import com.jcabi.github.mock.MkGithub;
import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class MkGithubTest {

    @Test
    public void testMockGithub() throws IOException {
        Tv tv = mock(Tv.class);
        when(tv.on()).thenReturn(true);
        MkGithub github = new MkGithub(tv);
        github.orgs().create("jcabi");
    }
}
```
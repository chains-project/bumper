```java
  import com.artipie.asto.factory.Storages;
import com.artipie.asto.fs.Directory;
import com.artipie.asto.fs.File;
import com.artipie.asto.fs.Path;
import com.artipie.asto.test.TestStorages;
import com.artipie.asto.test.TestTemp;
import com.artipie.asto.test.UncheckedTest;
import com.artipie.http.Headers;
import com.artipie.http.Response;
import com.artipie.http.Slice;
import com.artipie.http.misc.Public;
import com.artipie.http.rq.RequestLine;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.rs.StandardRs;
import java.io.IOException;
import java.nio.file.Path;
import java.util.concurrent.CompletableFuture;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

class YamlPolicyFactoryTest implements UncheckedTest {

    @Test
    void loadsYaml() throws IOException {
        final Path tmp = new TestTemp().asPath();
        final Path file = tmp.resolve("policy.yaml");
        file.toFile().createNewFile();
        MatcherAssert.assertThat(
            new YamlPolicyFactory(
                new Storages(
                    new File(file),
                    new Directory(tmp)
                )
            ).create(new RequestLine("GET", "/policy.yaml", "HTTP/1.1")).toCompletableFuture(),
            Matchers.equalTo(
                new StandardRs(
                    RsStatus.OK,
                    new Headers.From(
                        new Headers.Single("Content-Type", "application/yaml")
                    ),
                    new Public(
                        new Slice.From(
                            new CompletableFuture.CompletedFuture<>(
                                new Response.Wrap(
                                    new Response.From(
                                        new byte[0],
                                        new Headers.From(
                                            new Headers.Single("Content-Length", "0")
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        );
    }
}
```
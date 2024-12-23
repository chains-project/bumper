```java
  import com.artipie.asto.factory.Storages;
import com.artipie.asto.factory.TempStorage;
import com.artipie.asto.fs.FileStorage;
import com.artipie.asto.misc.UncheckedIO;
import com.artipie.http.Headers;
import com.artipie.http.Response;
import com.artipie.http.Slice;
import com.artipie.http.rq.RequestLine;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.rs.RsWithHeaders;
import com.artipie.http.rs.RsWithStatus;
import com.artipie.security.Auth;
import com.artipie.security.Policy;
import com.artipie.security.policy.PolicyFromYaml;
import com.artipie.security.policy.YamlPolicyFactory;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;

public final class YamlPolicySlice implements Slice {

  private final Policy policy;
  private final Path path;
  private final TempStorage temp;

  public YamlPolicySlice(final Policy policy, final Path path, final TempStorage temp) {
    this.policy = policy;
    this.path = path;
    this.temp = temp;
  }

  @Override
  public CompletionStage<Response> response(final RequestLine line, final Headers headers,
      final Auth auth) {
    return CompletableFuture.supplyAsync(() -> {
      try {
        final Map<String, Object> map = new YamlPolicyFactory(new FileStorage(this.path))
            .asMap(auth.name());
        return new RsWithStatus(RsStatus.OK, new RsWithHeaders(
            Optional.ofNullable(map.get("headers")).map(Headers.class::cast).orElse(Headers.EMPTY),
            new Response() {
              @Override
              public CompletionStage<Void> send(final Headers headers, final Accumulator accumulator) {
                return CompletableFuture.runAsync(() -> {
                  try {
                    accumulator.accept(map.get("body").toString().getBytes());
                  } catch (final IOException e) {
                    throw new UncheckedIO(e);
                  }
                });
              }
            }));
      } catch (final IOException e) {
        return new RsWithStatus(RsStatus.INTERNAL_ERROR, e);
      }
    });
  }

  public static CompletionStage<Slice> create(final Path path, final TempStorage temp) {
    return CompletableFuture.supplyAsync(() -> {
      try {
        return new YamlPolicySlice(new PolicyFromYaml(new FileStorage(path)), path, temp);
      } catch (final IOException e) {
        throw new UncheckedIO(e);
      }
    });
  }

  public static CompletionStage<Path> createTemp(final TempStorage temp) {
    return CompletableFuture.supplyAsync(() -> {
      try {
        final Path path = Files.createTempFile("policy", ".yaml");
        Files.write(path, "admin:\n  headers:\n    X-Auth-User: admin".getBytes());
        return path;
      } catch (final IOException e) {
        throw new UncheckedIO(e);
      }
    });
  }
}
```
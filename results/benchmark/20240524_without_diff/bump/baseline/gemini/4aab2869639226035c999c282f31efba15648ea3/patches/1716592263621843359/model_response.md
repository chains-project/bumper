```java
import com.artipie.asto.factory.Storages;
import com.artipie.asto.file.FileStorage;
import com.artipie.asto.fs.Directory;
import com.artipie.asto.misc.UncheckedIO;
import com.artipie.security.policy.Policy;
import com.artipie.security.policy.YamlPolicy;
import com.google.common.base.Charsets;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.concurrent.CompletableFuture;

public class YamlPolicyFactory {

  private final Directory directory;

  public YamlPolicyFactory(final Directory directory) {
    this.directory = directory;
  }

  public CompletableFuture<Policy> create() {
    return CompletableFuture.supplyAsync(() -> {
      try {
        final Path path = this.directory.join("policy.yaml").name();
        final FileStorage storage = new FileStorage(path);
        if (!Files.exists(path)) {
          Files.write(path, "default: ALLOW".getBytes(Charsets.UTF_8));
        }
        return new YamlPolicy(Storages.wrap(storage));
      } catch (final IOException e) {
        throw UncheckedIO.from(e);
      }
    });
  }
}
```
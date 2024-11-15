```java
import com.artipie.asto.factory.Storages;
import com.artipie.http.Headers;
import com.artipie.http.Response;
import com.artipie.http.Slice;
import com.artipie.http.async.AsyncResponse;
import com.artipie.http.headers.ContentDisposition;
import com.artipie.http.headers.ContentType;
import com.artipie.http.headers.Header;
import com.artipie.http.headers.Upgrade;
import io.reactivex.Flowable;
import java.nio.ByteBuffer;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Optional;
import java.util.concurrent.CompletionStage;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public final class YamlPolicyFactory implements Slice {
  private final Storages storages;

  public YamlPolicyFactory(Storages storages) {
    this.storages = storages;
  }

  @Override
  public Response response(String line, Iterable<Map.Entry<String, String>> headers,
      Function<ByteBuffer, CompletionStage<Void>> channel) {
    return new AsyncResponse(
        Flowable.fromIterable(this.storages.list())
            .flatMap(key -> this.storages.value(key).value(key + ".yaml").get())
            .map(bytes -> new Response(
                Response.OK,
                new Headers.From(
                    new ContentType("text/yaml"),
                    new ContentDisposition("attachment", key + ".yaml"),
                    new Upgrade("websocket"),
                    Stream.concat(
                        headers.stream(),
                        this.storages.value(key).value(key + ".headers").get().stream()
                            .map(bytes1 -> new Header(bytes1.toString()))
                    ).collect(Collectors.toList())
                ),
                Optional.of(bytes))),
        1,
        TimeUnit.SECONDS);
  }
}
```
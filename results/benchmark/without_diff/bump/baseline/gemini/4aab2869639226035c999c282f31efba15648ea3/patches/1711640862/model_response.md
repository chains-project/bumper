```java
import com.artipie.asto.factory.Storages;
import com.artipie.http.Headers;
import com.artipie.http.Response;
import com.artipie.http.Slice;
import com.artipie.http.async.AsyncResponse;
import com.artipie.http.headers.Header;
import com.artipie.http.headers.StandardHeaders;
import com.artipie.http.hm.RsHasHeaders;
import com.artipie.http.hm.SliceHasHeaders;
import com.artipie.http.hm.SliceHasResponse;
import com.artipie.http.rq.RequestLine;
import com.artipie.http.rq.RqMethod;
import com.artipie.http.rq.RqWithHeaders;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.rs.RsWithBody;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;

public final class YamlPolicyFactory implements Slice {

  private final Storages storages;
  private final String name;

  public YamlPolicyFactory(Storages storages, String name) {
    this.storages = storages;
    this.name = name;
  }

  @Override
  public Response response(RequestLine line, Iterable<Map.Entry<String, String>> headers) {
    return new SliceHasResponse(new SliceHasHeaders(this, new StandardHeaders.ForSingle(
        new Header.Single("Content-Type", "text/plain; charset=utf-8")))) {

      @Override
      public Response response(RqWithHeaders rq) {
        return new AsyncResponse(
            storages.get(name)
                .value()
                .thenApply(data -> new RsWithBody(
                    RsStatus.OK,
                    Headers.EMPTY,
                    data.toByteArray(StandardCharsets.UTF_8)))
                .thenApply(RsHasHeaders::new)
                .thenApply(SliceHasResponse::new)
                .thenApply(SliceHasResponse::response)
                .exceptionally(err -> {
                  err.printStackTrace();
                  return new RsWithBody(
                      RsStatus.INTERNAL_ERROR,
                      Headers.EMPTY,
                      "Error while reading policy".getBytes(StandardCharsets.UTF_8));
                }));
      }
    }.response(line, headers);
  }
}
```
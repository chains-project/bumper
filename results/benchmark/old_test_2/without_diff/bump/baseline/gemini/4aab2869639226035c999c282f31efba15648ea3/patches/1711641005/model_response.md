```java
  import com.artipie.asto.factory.Storages;
  import com.artipie.asto.storage.Storage;
  import com.artipie.asto.storage.ValueAndEnvelope;
  import com.artipie.asto.storage.key.Key;
  import com.artipie.asto.storage.value.ValueFrom;
  import com.artipie.http.Headers;
  import com.artipie.http.Response;
  import com.artipie.http.Slice;
  import com.artipie.http.async.AsyncResponse;
  import com.artipie.http.headers.ContentType;
  import com.artipie.http.headers.Header;
  import com.artipie.http.hm.RsHasHeaders;
  import com.artipie.http.hm.RsHasStatus;
  import com.artipie.http.hm.SliceHasResponse;
  import com.artipie.http.rq.RequestLineFrom;
  import com.artipie.http.rq.RqMethod;
  import com.artipie.http.rs.RsStatus;
  import com.artipie.http.rs.RsWithBody;
  import com.artipie.http.rs.RsWithHeaders;
  import com.artipie.http.rs.RsWithStatus;
  import com.artipie.http.rs.RsWithoutBody;
  import com.artipie.http.rs.StandardRs;
  import com.artipie.http.rs.xjson.RsJson;
  import com.artipie.http.rs.xjson.Xjson;
  import com.artipie.http.slice.SliceSimple;
  import com.artipie.http.slice.SliceTimeout;
  import com.artipie.http.slice.SliceWithResponse;
  import com.artipie.http.slice.SliceWithTimeout;
  import com.artipie.http.slice.SliceWrap;
  import com.artipie.http.slice.WithHeaders;
  import com.artipie.http.slice.WithStatus;
  import com.google.common.collect.ImmutableMap;
  import com.google.common.collect.ImmutableSet;
  import java.nio.ByteBuffer;
  import java.nio.charset.StandardCharsets;
  import java.util.Map;
  import java.util.Set;
  import java.util.concurrent.CompletableFuture;
  import java.util.concurrent.CompletionStage;
  import java.util.concurrent.ExecutionException;
  import java.util.concurrent.TimeUnit;
  import java.util.concurrent.TimeoutException;
  import java.util.concurrent.atomic.AtomicReference;
  import java.util.function.Function;
  import org.json.JSONObject;
  import org.reactivestreams.Publisher;

  /**
   * HTTP slice that provides a YAML file from a storage.
   *
   * @since 0.11
   */
  public final class YamlSlice implements Slice {

    private final Storage storage;

    public YamlSlice(final Storage storage) {
      this.storage = storage;
    }

    @Override
    public Response response(final String line, final Iterable<String> headers,
        final Publisher<ByteBuffer> body) {
      final RequestLineFrom request = new RequestLineFrom(line);
      final Headers header = new Headers(headers);
      final Key key = new Key.From(request.uri());
      final CompletableFuture<Response> result = new CompletableFuture<>();
      final AtomicReference<String> yaml = new AtomicReference<>();
      this.storage.value(key)
          .thenAccept(new ValueFrom.EnvelopeConsumer() {
            @Override
            public void accept(final ValueAndEnvelope value) {
              yaml.set(new String(value.value().array(), StandardCharsets.UTF_8));
              result.complete(new WithHeaders(
                  new WithStatus(
                      new SliceWithResponse(
                          new SliceSimple(
                              new RsWithBody(
                                  new RsJson(
                                      new Xjson.From(
                                          new JSONObject(yaml.get())
                                      )
                                  )
                              )
                          ),
                          new RsHasStatus(RsStatus.OK)
                      ),
                      header.get(ContentType.NAME)
                          .map(new Function<Header, RsHasStatus>() {
                            @Override
                            public RsHasStatus apply(final Header header) {
                              return new WithStatus(
                                  new RsWithHeaders(
                                      new RsHasStatus(RsStatus.OK),
                                      new ImmutableSet.Builder<Header>()
                                          .addAll(header)
                                          .add(
                                              new ContentType(
                                                  yaml.get().length()
                                                      + " "
                                                      + "text/yaml"
                                              )
                                          )
                                          .build()
                                  ),
                                  RsStatus.OK
                              );
                            }
                          })
                          .orElse(new RsHasStatus(RsStatus.OK))
                  ),
                  new ImmutableSet.Builder<Header>()
                      .addAll(header)
                      .add(new ContentType("text/yaml"))
                      .build()
              ).response());
            }
          })
          .exceptionally(new Function<Throwable, Response>() {
            @Override
            public Response apply(final Throwable throwable) {
              return new StandardRs(RsStatus.NOT_FOUND);
            }
          });
      try {
        return result.get(500L, TimeUnit.MILLISECONDS);
      } catch (final InterruptedException | ExecutionException | TimeoutException e) {
        return new StandardRs(RsStatus.INTERNAL_ERROR);
      }
    }
  }
```
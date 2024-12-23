```java
import com.artipie.asto.factory.Storages;
import com.artipie.asto.test.TestResource;
import com.artipie.asto.test.TestStorage;
import com.artipie.http.Headers;
import com.artipie.http.Response;
import com.artipie.http.Slice;
import com.artipie.http.rq.RequestLine;
import com.artipie.http.rq.RqMethod;
import com.artipie.http.rs.RsStatus;
import com.artipie.security.Policy;
import com.artipie.security.policy.YamlPolicyFactory;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;

public final class YamlPolicyFactoryTest implements Slice {

    private final Policy policy;

    public YamlPolicyFactoryTest(final Policy policy) {
        this.policy = policy;
    }

    @Override
    public CompletionStage<Response> response(final RequestLine line, final Headers headers) {
        return new TestResource(
            "com/artipie/security/policy/test.yaml"
        ).asInputStream()
            .thenApply(TestStorage::new)
            .thenApply(Storages::new)
            .thenApply(
                storage -> new YamlPolicyFactory(storage).create(
                    new RequestLine(RqMethod.GET, "/test"),
                    headers
                )
            )
            .thenCompose(policy -> policy.response(line, headers))
            .thenApply(
                response -> response.with(
                    RsStatus.OK,
                    new TestResource("com/artipie/security/policy/test-response.yaml").asBytes()
                )
            )
            .exceptionally(
                throwable -> new CompletableFuture<Response>() {
                    {
                        this.complete(
                            new Response(RsStatus.INTERNAL_ERROR, throwable.getMessage())
                        );
                    }
                }
            );
    }
}
```
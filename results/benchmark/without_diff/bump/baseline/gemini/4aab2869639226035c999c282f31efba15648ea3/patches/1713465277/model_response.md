```java
  import com.artipie.http.Response;
  import com.artipie.http.Slice;
  import com.artipie.http.rq.RequestLineFrom;
  import com.artipie.http.rs.RsStatus;
  import com.artipie.http.rs.RsWithBody;
  import com.artipie.security.policy.Policy;
  import com.artipie.security.policy.PolicyFromYaml;
  import com.google.common.base.Joiner;
  import java.io.IOException;
  import java.nio.charset.StandardCharsets;
  import java.util.concurrent.CompletableFuture;
  import java.util.concurrent.CompletionStage;

  public final class YamlPolicyFactory implements Slice {
    private final Policy policy;

    public YamlPolicyFactory(final Policy policy) {
      this.policy = policy;
    }

    @Override
    public CompletionStage<Response> response(final RequestLineFrom request) {
      return CompletableFuture.completedFuture(
          new RsWithBody(
              new RsStatus.Success(200),
              String.format(
                  "{\"rules\": [%s]}",
                  Joiner.on(",").join(
                      this.policy.rules().stream()
                          .map(rule -> String.format(
                              "{\"origin\": \"%s\", \"methods\": [%s]}",
                              rule.origin(),
                              Joiner.on(",").join(rule.methods())
                          ))
                          .iterator()
                  )
              ).getBytes(StandardCharsets.UTF_8)
          )
      );
    }
  }
```
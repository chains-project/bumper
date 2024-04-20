Here's the updated method with the necessary changes to fix the error:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()),
        new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action),
        new BearerAuthScheme((token) -> CompletableFuture.completedFuture(
            Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                .filter(user -> token.equals(token(user)))
                .map(user -> new AuthUser(user.name()))
                .collect(Collectors.toList())
        ), ""));
}
```
The main change is the use of `AuthUser` instead of `Authentication.User` in the `Authentication.Single` constructor and the `AuthUser` constructor. Also, the `Stream.findFirst()` method is replaced with `Stream.collect(Collectors.toList())` to collect the matched users into a list.

Note: I imported the necessary classes for brevity. Make sure to import them in your code.

```java
import java.util.stream.Stream;
import java.util.List;
import java.util.stream.Collectors;
import java.util.concurrent.CompletableFuture;
import static java.util.Collections.emptyList;
import static java.util.Collections.singletonList;
import static java.util.Objects.requireNonNull;
import static java.util.Optional.ofNullable;

import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoDocker;
import com.artipie.docker.http.DockerSlice;
import com.artipie.http.auth.Authentication;
import com.artipie.http.auth.BearerAuthScheme;
import com.artipie.http.auth.AuthUser;
import com.artipie.http.auth.Authentication.Single;
import com.artipie.http.Slice;
import com.artipie.http.auth.Token;
import com.artipie.http.rq.RequestLine;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.rt.ByMethod;
import com.artipie.http.rt.Chain;
import com.artipie.http.rt.RsDirect;
import com.artipie.http.rt.RsString;
import com.artipie.http.rt.Route;
import com.artipie.http.rt.Routes;
import com.artipie.http.AuthScheme;
import com.artipie.http.auth.Authentication;
import java.util.Optional;
import java.util.function.Function;
import java.util.function.Predicate;
import static java.util.Collections.singleton;
import static java.util.Collections.emptySet;
import static java.util.stream.Stream.of;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.CompletionStage;
```
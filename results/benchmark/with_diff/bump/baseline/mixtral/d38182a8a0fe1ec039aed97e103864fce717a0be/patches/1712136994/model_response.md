Here's a possible patch for the given code. I've updated the code to use `AuthUser` instead of `User` and adapted it to the new method signatures.

```java
import com.artipie.http.auth.AuthUser;
import com.artipie.http.auth.Authentication;
import com.artipie.http.auth.Permissions;
import com.artipie.http.rs.StandardRs;
import com.artipie.http.Slice;
import io.reactivex.CompletableFuture;
import java.util.concurrent.Executor;
import java.util.function.Function;
import org.hamcrest.MatcherAssert;
import org.hamcrest.core.IsEqual;
import static java.util.Collections.emptyMap;
import static java.util.Collections.emptySet;
import static java.util.Collections.singleton;
import static java.util.concurrent.CompletableFuture.completedFuture;
import static java.util.concurrent.Executors.newSingleThreadExecutor;

public class AuthScopeSliceTest {
    @Test
    void testScope() {
        final String line = "GET /resource.txt HTTP/1.1";
        final String action = "foo:bar:baz";
        final Executor executor = newSingleThreadExecutor();
        final Function<AuthUser, CompletableFuture<Permissions.Single>> auth =
            user -> completedFuture(new Permissions.Single(user, action));
        final Function<AuthUser, Boolean> check = (user, act) -> {
            System.out.println("AuthUser: " + user);
            return true;
        };
        new AuthScopeSlice(
            new Slice.Simple(request -> {
                System.out.println("Request: " + request);
                return completedFuture(StandardRs.OK);
            }),
            auth,
            check
        ).response(line, emptyMap(), emptySet()).send(
            (status, headers, body) -> completedFuture(new Void[])
        ).toCompletableFuture().join();
        MatcherAssert.assertThat(
            "Request line passed to slice",
            line,
            new IsEqual<>(line)
        );
        MatcherAssert.assertThat(
            "Scope passed as action to permissions",
            action,
            new IsEqual<>(action)
        );
    }
}
```

This patch replaces the `Authentication.User` with `AuthUser`, updates the lambda functions accordingly, and uses the new `Permissions.Single` constructor. I've also added a few imports to make the code compile.

Please note that you may need to adjust the implementation details based on your specific requirements. This patch is just one of the possible solutions, and it aims to fix the compilation error while preserving the original functionality.
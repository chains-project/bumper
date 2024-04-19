Here's a possible patch for the code:

```java
import com.artipie.http.auth.AuthUser;
import com.artipie.http.auth.Authentication;
import com.artipie.http.auth.Authentication.Single;
import com.artipie.http.auth.Permissions;
import com.artipie.http.auth.Permission;
import com.artipie.http.auth.OperationControl;
import com.artipie.http.auth.JoinedPermissions;
import com.artipie.http.auth.UserPermissions;
import com.artipie.http.auth.User;
import com.artipie.http.auth.User$Simple;
import com.artipie.http.auth.Roles;
import com.artipie.http.Slice;
import com.artipie.http.rq.RequestLine;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.rs.StandardRs;
import com.artipie.http.rs.Rs;
import com.artipie.http.Header;
import com.artipie.http.Headers;
import com.artipie.http.rt.ByFunction;
import com.artipie.http.rt.RsHandler;
import com.artipie.http.rt.RsOp;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executor;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.Stream;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import reactor.core.publisher.Mono;

@Test
void testScope() {
    final String line = "GET /resource.txt HTTP/1.1";
    final String action = "foo:bar:baz";
    final AtomicReference<String> caction = new AtomicReference<>();
    final AtomicReference<String> cline = new AtomicReference<>();
    final User alice = new User$Simple(Roles.of("user"), Permissions.of());
    final OperationControl opControl = new OperationControl(new JoinedPermissions(Stream.of(
        new Permission.All(),
        new Permission.ByName("foo"),
        new Permission.ByName("bar"),
        new Permission.ByName("baz")
    )));
    new AuthScopeSlice(
        new Slice.Simple(requestLine -> {
            cline.set(requestLine.toString());
            return new Rs.Response(RsStatus.OK);
        }),
        (headers, requestLine) -> CompletableFuture.completedFuture(
            new Single(alice, "")
        ),
        (user, act) -> {
            caction.set(act);
            return opControl.allowed(user);
        }
    ).response(line, Headers.EMPTY, Content.EMPTY).send(
        (status, headers, body) -> Mono.fromRunnable(() -> {})
    ).block();
    MatcherAssert.assertThat(
        "Request line passed to slice",
        cline.get(),
        new Matchers.IsEqual<>(line)
    );
    MatcherAssert.assertThat(
        "Scope passed as action to permissions",
        caction.get(),
        new Matchers.IsEqual<>(action)
    );
}
```

The main changes are:

* Importing the new `AuthUser` class and the updated `Single` and `Permissions` classes from the updated library.
* Creating a `User` object for Alice using the new `User$Simple` constructor.
* Creating a new `OperationControl` object with a `JoinedPermissions` object that allows access if any of the permissions are granted.
* Updating the lambda function that creates the `Single` object to use the new `Single` constructor.
* Updating the lambda function that checks if the action is allowed to use the new `allowed` method of the `OperationControl` object.
* Updating the `send` method to use the new `block` method of the `CompletableFuture` object.
* Updating the `MatcherAssert` and `Matchers` imports to use the new `IsEqual` matcher.

Note that these changes are not the only possible way to fix the code. There may be other valid ways to update the code to use the new library version.
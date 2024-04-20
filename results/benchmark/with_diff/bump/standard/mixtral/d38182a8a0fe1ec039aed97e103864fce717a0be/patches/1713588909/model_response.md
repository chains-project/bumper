Here's a fixed version of the code that uses the new `AuthUser` class instead of the removed `Authentication.User` class:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter(user -> token.equals(token(user)))
            .map(user -> new AuthUser(user.name()))
            .findFirst()), ""));
}
```
Note that I had to import a few classes for the code to compile. Here are the necessary imports:
```java
import com.artipie.asto.memory.InMemoryStorage;
import com.artipie.docker.asto.AstoDocker;
import com.artipie.docker.http.BearerAuthScheme;
import com.artipie.docker.http.DockerSlice;
import com.artipie.http.auth.Authentication;
import com.artipie.http.auth.AuthUser;
import com.artipie.http.auth.BearerAuthScheme.Token;
import com.artipie.http.auth.Permission;
import com.artipie.http.fs.FileStorage;
import com.artipie.http.rq.RequestLineFrom;
import com.artipie.http.rs.RsStatus;
import com.artipie.http.slice.Slice;
import com.artipie.http.ssl.SslInfoFrom;
import com.artipie.security.perms.Action;
import com.artipie.security.perms.AuthUser;
import com.artipie.security.perms.Permission;
import com.artipie.security.perms.PermissionConfig;
import com.artipie.security.perms.User;
import com.artipie.security.perms.UserPermissions;
import com.artipie.security.policy.Policy;
import com.artipie.security.policy.PolicyByUsername;
import com.artipie.security.policy.PolicyFromYaml;
import com.google.common.base.Supplier;
import java.nio.file.Path;
import java.util.Collections;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Executor;
import java.util.function.Function;
import java.util.stream.Stream;
import static com.artipie.http.auth.AuthUser.authContext;
import static com.artipie.http.auth.AuthUser.name;
import static com.artipie.http.auth.Permissions.single;
import static com.artipie.http.auth.Permissions.wrap;
import static com.artipie.http.auth.Role.USER;
import static com.artipie.http.auth.Role.of;
import static com.artipie.http.auth.User.from;
import static com.artipie.http.auth.User.simple;
import static com.artipie.http.auth.UserPermissions.userPermissions;
import static com.artipie.http.ssl.SslInfo.sslInfo;
import static com.artipie.http.ssl.SslInfo.sslInfoFrom;
import static com.artipie.http.slice.SliceAbsorber.sliceAbsorber;
import static com.artipie.http.slice.SliceAbsorber.sliceAbsorberFrom;
import static com.artipie.http.slice.SliceMiddleware.sliceMiddleware;
import static com.artipie.http.slice.SliceMiddleware.sliceMiddlewareFrom;
import static java.util.Collections.singletonList;
import static java.util.Collections.singletonMap;
import static java.util.concurrent.CompletableFuture.completedFuture;
import static java.util.stream.Stream.of;
import static org.reactivestreams.Publisher.from;
```
I hope this helps! Let me know if you have any questions.
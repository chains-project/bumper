```java
import com.artipie.http.auth.AuthUser;
import com.artipie.http.auth.Authentication$Single;

...

        return new Authentication$Single(new AuthUser("alice"), "");
```
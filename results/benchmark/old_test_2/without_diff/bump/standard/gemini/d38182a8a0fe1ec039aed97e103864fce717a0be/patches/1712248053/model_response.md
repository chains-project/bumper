```java
import com.artipie.http.auth.Authentication;

...

        @java.lang.Override
        public Optional<Authentication.User> user() {
            return java.util.Optional.of(new Authentication.User("alice"));
        }

        @java.lang.Override
        public java.lang.String challenge() {
            return "";
        }
```
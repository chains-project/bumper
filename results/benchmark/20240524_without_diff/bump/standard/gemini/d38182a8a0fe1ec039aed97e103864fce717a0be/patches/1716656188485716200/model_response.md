```java
// TODO: review this AI generated patch!
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    if (action.equals("login")) {
        return this.login();
    } else if (action.equals("logout")) {
        return this.logout();
    } else if (action.equals("user")) {
        return this.user();
    } else {
        return this.error();
    }
}
```
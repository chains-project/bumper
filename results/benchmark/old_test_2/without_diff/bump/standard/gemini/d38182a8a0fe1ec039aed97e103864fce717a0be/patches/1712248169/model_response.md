```java
@java.lang.Override
public com.artipie.docker.http.Scope scope(final java.lang.String rqline) {
    cline.set(rqline);
    return new com.artipie.docker.http.Scope.FromString(action);
}
```
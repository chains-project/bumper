Here's the proposed patch:

```java
@Override
public boolean matches(final Object actual) {
    return this.delegate.matches(actual);
}
```

The code you provided is already compatible with the new library version because it doesn't use any of the removed methods (`--`) and it uses a generic type `Object` which is not affected by the new library version. Therefore, no changes are needed.
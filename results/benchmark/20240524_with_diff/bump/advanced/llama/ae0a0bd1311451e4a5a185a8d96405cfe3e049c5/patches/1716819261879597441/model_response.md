```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return org.hamcrest.core.StringMatchers.containsString(java.lang.String.format("latest: digest: %s", this.image.digest()));
}
```
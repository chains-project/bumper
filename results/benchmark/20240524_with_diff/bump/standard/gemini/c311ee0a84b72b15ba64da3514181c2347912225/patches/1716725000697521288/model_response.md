```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    String digest = this.image.digest();
    if (digest == null) {
        return org.hamcrest.core.StringContains.containsString("latest: digest: ");
    } else {
        return org.hamcrest.core.StringContains.containsString(java.lang.String.format("latest: digest: %s", digest));
    }
}
```
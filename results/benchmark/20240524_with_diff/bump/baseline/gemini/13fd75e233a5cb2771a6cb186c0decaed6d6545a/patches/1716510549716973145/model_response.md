```java
  private Matcher<String> manifestPushed() {
        String digest = String.format("latest: digest: %s", this.image.digest());
        return new StringContains(false, digest);
    }
```
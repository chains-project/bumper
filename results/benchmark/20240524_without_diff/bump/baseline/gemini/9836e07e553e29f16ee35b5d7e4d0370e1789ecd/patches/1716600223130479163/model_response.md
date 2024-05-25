```java
  private Matcher<String> manifestPushed() {
        Image image = this.image;
        return new StringContains(false, String.format("latest: digest: %s", image.digest()));
    }
```
```java
  private Matcher<String> layersPushed() {
        boolean isNegative = false;
        String expectedMessage = String.format("%s: Pushed", this.image.layer());
        return new StringContains(isNegative, expectedMessage);
    }
```
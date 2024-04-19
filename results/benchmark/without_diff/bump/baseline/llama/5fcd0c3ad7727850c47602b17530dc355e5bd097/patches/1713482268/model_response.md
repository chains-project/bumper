Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(data.getMutatedClass())));
}
```

Change the line:
```
coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
```
to
```
coverage.getClassInfo(Collections.singleton(data.getMutatedClass()), this.getClass().getClassLoader());
```
Added `this.getClass().getClassLoader()` as an argument to the `getClassInfo()` method to pass the class loader of the current class, which should fix the error.
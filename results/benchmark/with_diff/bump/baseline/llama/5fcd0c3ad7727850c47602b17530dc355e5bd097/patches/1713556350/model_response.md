Here's a possible patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    final var classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the call to `getClassInfo(Collections.singleton(data.getMutatedClass()))` and instead calls `getClassInfo(data.getMutatedClass())` directly. This is possible because the `getClassInfo` method in the `CoverageDatabase` class has been updated to take a single `ClassName` argument instead of a `Collection` of `ClassName`s.

The patch also removes the `Override` annotation, as it is not needed.

This patch should fix the error and allow the code to compile and run correctly.
Here's a possible patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `getClassInfo(Collections.singleton(data.getMutatedClass()));` call, which is not available in the new library version, and instead uses the `getClassInfo(data.getMutatedClass());` method, which is available in the new version.

The `getClassInfo(ClassName)` method is added in the new library version, and it takes a `ClassName` parameter instead of a `Collection<ClassName>` parameter. Therefore, we need to remove the `Collections.singleton(data.getMutatedClass());` part and pass `data.getMutatedClass()` directly to the `getClassInfo()` method.

This patch should fix the error and allow the code to compile and run correctly with the new library version.
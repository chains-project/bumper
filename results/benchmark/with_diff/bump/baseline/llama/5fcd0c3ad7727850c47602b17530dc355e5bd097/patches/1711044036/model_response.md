Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(
        data.getFileName(),
        data.getMutations(),
        classInfo.getClassName()
    );
}
```
The patch removes the `getClassInfo(java.util.Set<org.pitest.classinfo.ClassName>)` method call, which is not available in the new library version. Instead, we use the `getClassInfo(ClassName)` method to get the `ClassInfo` object for the mutated class.

Additionally, we had to remove the `Collections.singleton(data.getMutatedClass()` call, as the `getClassInfo()` method now takes a `ClassName` parameter instead of a `java.util.Collection`.

This patch should fix the error and allow the code to compile and run correctly with the new library version.
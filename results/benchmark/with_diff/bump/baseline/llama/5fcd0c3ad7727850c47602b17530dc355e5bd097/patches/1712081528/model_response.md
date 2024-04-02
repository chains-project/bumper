Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `getClassInfo(java.util.Set<org.pitest.classinfo.ClassName>)` method call, which is not available in the new library version, and instead uses the `getClassInfo(org.pitest.classinfo.ClassName)` method, which is added in the new version.

Additionally, the patch removes the `Collections.singleton(data.getMutatedClass())` argument passed to the `getClassInfo()` method, as it is not needed.

This patch should fix the error and allow the code to compile and run correctly with the new library version.
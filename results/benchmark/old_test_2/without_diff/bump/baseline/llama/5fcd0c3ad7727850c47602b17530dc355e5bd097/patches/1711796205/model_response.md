Here's a possible patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    final String className = data.getMutatedClass().getCanonicalName();
    final ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(className));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the usage of `getClassInfo(Collections.singleton(data.getMutatedClass()))` which is not available in the version of the dependency that the code is using. Instead, it uses `getClassInfo(Collections.singleton(className))` which is available in the same version.

It's important to note that this patch assumes that the `CoverageDatabase` object has a method `getClassInfo(Collection<String> classNames)` that returns a `ClassInfo` object for the given class names. If this method is not available, a different patch would be required.
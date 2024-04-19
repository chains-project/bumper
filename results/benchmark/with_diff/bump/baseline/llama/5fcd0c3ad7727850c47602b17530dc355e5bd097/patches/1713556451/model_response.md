Here's a possible patch to fix the error:
```
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the call to `getClassInfo(Collections.singleton(data.getMutatedClass()))` and instead calls `getClassInfo(data.getMutatedClass())` directly.
The `getClassInfo` method signature has changed in the new library version, and it now takes a `ClassName` parameter instead of a `Collection` of `ClassName`s.
By calling `getClassInfo` with a single `ClassName` parameter, we avoid the need to create a `Collection` of `ClassName`s and avoid the compatibility issue with the new library version.

Additionally, the patch removes the `Override` annotation, as the method is not overriding any method in the new version.

Please note that this patch is just a suggestion, and it's up to you to test and validate it before applying it to your codebase.
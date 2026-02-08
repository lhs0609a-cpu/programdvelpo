/**
 * Google Apps Script - 문의 폼 데이터를 구글 시트에 저장
 *
 * === 설정 방법 ===
 *
 * 1. Google 스프레드시트 생성
 *    - https://sheets.google.com 에서 새 스프레드시트 생성
 *    - 첫 번째 행에 헤더 입력: 타임스탬프 | 회사명 | 담당자명 | 연락처 | 이메일 | 문의유형 | 문의내용
 *
 * 2. Apps Script 열기
 *    - 스프레드시트에서 [확장 프로그램] > [Apps Script] 클릭
 *
 * 3. 코드 붙여넣기
 *    - 기존 코드를 모두 삭제하고 아래 코드를 붙여넣기
 *
 * 4. 웹 앱으로 배포
 *    - [배포] > [새 배포] 클릭
 *    - 유형: 웹 앱 선택
 *    - 실행 사용자: 본인
 *    - 액세스 권한: 모든 사용자 (익명 포함)
 *    - [배포] 클릭
 *
 * 5. URL 복사
 *    - 생성된 웹 앱 URL을 복사
 *    - index.html의 GOOGLE_SCRIPT_URL 변수에 붙여넣기
 *
 * === 주의사항 ===
 * - 코드 수정 후에는 반드시 새 버전으로 재배포 필요
 * - 배포 시 "새 배포"가 아닌 "배포 관리"에서 버전 업데이트 가능
 */

// 스프레드시트 ID (URL에서 /d/ 와 /edit 사이의 문자열)
// 예: https://docs.google.com/spreadsheets/d/ABC123/edit → ABC123
const SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID_HERE';

// 데이터를 저장할 시트 이름
const SHEET_NAME = 'Sheet1';

/**
 * POST 요청 처리 - 폼 데이터 수신
 */
function doPost(e) {
  try {
    // 요청 데이터 파싱
    const data = JSON.parse(e.postData.contents);

    // 스프레드시트 열기
    const spreadsheet = SpreadsheetApp.openById(SPREADSHEET_ID);
    const sheet = spreadsheet.getSheetByName(SHEET_NAME);

    // 데이터 행 추가
    sheet.appendRow([
      data.timestamp || new Date().toLocaleString('ko-KR'),
      data.company || '',
      data.name || '',
      data.phone || '',
      data.email || '',
      data.type || '',
      data.message || ''
    ]);

    // 이메일 알림 발송 (선택사항 - 아래 주석 해제하여 사용)
    // sendNotificationEmail(data);

    // 성공 응답
    return ContentService
      .createTextOutput(JSON.stringify({
        status: 'success',
        message: '데이터가 성공적으로 저장되었습니다.'
      }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    // 오류 응답
    return ContentService
      .createTextOutput(JSON.stringify({
        status: 'error',
        message: error.toString()
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * GET 요청 처리 - 테스트용
 */
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({
      status: 'success',
      message: 'Google Apps Script가 정상 작동 중입니다.'
    }))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * 이메일 알림 발송 (선택사항)
 * 새 문의가 들어오면 지정된 이메일로 알림 발송
 */
function sendNotificationEmail(data) {
  const recipient = 'your-email@example.com'; // 알림 받을 이메일 주소
  const subject = `[새 문의] ${data.company} - ${data.type}`;

  const body = `
새로운 문의가 접수되었습니다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

■ 접수 시간: ${data.timestamp}

■ 회사명: ${data.company}

■ 담당자: ${data.name}

■ 연락처: ${data.phone}

■ 이메일: ${data.email}

■ 문의 유형: ${data.type}

■ 문의 내용:
${data.message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  `;

  MailApp.sendEmail(recipient, subject, body);
}

/**
 * 테스트 함수 - Apps Script 에디터에서 직접 실행하여 테스트
 */
function testDoPost() {
  const testData = {
    postData: {
      contents: JSON.stringify({
        timestamp: new Date().toLocaleString('ko-KR'),
        company: '테스트 회사',
        name: '홍길동',
        phone: '010-1234-5678',
        email: 'test@example.com',
        type: '맞춤 프로그램 개발',
        message: '테스트 문의입니다.'
      })
    }
  };

  const result = doPost(testData);
  console.log(result.getContent());
}
